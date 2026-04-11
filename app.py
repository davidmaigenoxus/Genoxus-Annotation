
import pandas as pd
import duckdb
import os

def calculate_buckets(start, end):
    # Given the start ane end calculate the first and last partial buckets and the middle buckets. 
    # Each bucket is of size 1 million.
    start_base = start // 1000000 + 1
    end_base = end // 1000000

    start_base *= 1000000
    end_base *= 1000000
    delta = 1000000

    print (f"start_base: {start_base}")
    print (f"end_base: {end_base}")


    # This is the middle list of buckets.
    pairs = [(i+1, i+delta) for i in range(start_base, end_base, delta)]
    if len(pairs) > 0:
        middle_bucket_names = [f"bp={pair[0]}-{pair[1]}" for pair in pairs]
        #print (f"middle_bucket_names: {middle_bucket_names}")
    else:
        print("No middle buckets.")


    # First partial bucket.
    lower_bound_start = start // 1000000 * 1000000 + 1
    lower_bound_end = (start // 1000000 + 1) * 1000000
    lower_bound_bucket_name = f"bp={lower_bound_start}-{lower_bound_end}"
    #print (f"lower_bound_bucket_name: {lower_bound_bucket_name}")

    # Last partial bucket.
    upper_bound_start = end // 1000000 * 1000000 + 1
    upper_bound_end = (end // 1000000 + 1) * 1000000
    upper_bound_bucket_name = f"bp={upper_bound_start}-{upper_bound_end}"
    #print (f"upper_bound_bucket_name: {upper_bound_bucket_name}")

    # if the middle list of buckets is empty, then the first partial bucket is either the same as the last partial bucket 
    # or there is no middle bucket. We need to check if the first partial bucket overlaps with the last partial bucket. 
    # If it does, then we only need to consider the first partial bucket. 
    # If it does not, then we need to consider both the first and last partial buckets.
    return lower_bound_bucket_name, middle_bucket_names, upper_bound_bucket_name, start_base, end_base



def parse_buckets_results(agg_results_df)-> pd.DataFrame:
    term_not_provided = "The term 'not provided'"
    term_not_specified = "The term 'not specified'"

    agg_text = []
    agg_ref_db = []
    agg_ref_accession = []


    for index in range(len(agg_results_df)):
        #pprint (agg_results_df['Classifications'][index][0]['Conditions']) # 0 index in the classifications list
        
        #print (f"Index: {index}")

        if len(agg_results_df['Classifications'][index][0]['Conditions']) > 0:
            for condition in agg_results_df['Classifications'][index][0]['Conditions']:

                """
                if condition['Attributes'] is not None and len(condition['Attributes']) > 0:
                    attributes = condition['Attributes']
                    for attribute in attributes:
                        if attribute is not None and attribute["Value"] is not None:
                            attribute_value = attribute["Value"]
                            if term_not_provided not in attribute_value and term_not_specified not in attribute_value:                        
                                print (attribute_value)
                                reference = attribute["XRefs"] 
                                print (f"Reference: {reference}")
                """


                if condition['Attributes'] is not None and len(condition['Attributes']) > 0:
                    attributes = condition['Attributes']
                    for attribute in attributes:
                        if attribute['Type'] == 'public definition' and term_not_provided not in attribute['Value'] and term_not_specified not in attribute['Value']:

                            #print (attribute)
                            
                            if len(agg_text)==0:
                                agg_text.append(attribute['Value'])   
                                agg_ref_db.append(attribute['XRefs'][0]['Database'])
                                agg_ref_accession.append(attribute['XRefs'][0]['Accession'])
                            else:
                                if attribute['Value'] not in agg_text:
                                    agg_text.append(attribute['Value'])
                                    agg_ref_db.append(attribute['XRefs'][0]['Database'])
                                    agg_ref_accession.append(attribute['XRefs'][0]['Accession'])

    if len(agg_text) > 0 and len(agg_ref_db) > 0:
        agg_findings_df = pd.DataFrame({
            'Text': agg_text,
            'References': agg_ref_db,
            'Accessions': agg_ref_accession
        })
        return agg_findings_df
    else:
        print ("No valid text and references found in the middle buckets results.")
        return pd.DataFrame() # empty dataframe




def search_middle_buckets(conn, base_dir_37, middle_bucket_names)-> pd.DataFrame:
    folders = []
    agg_results_df = pd.DataFrame()
    
    if len(middle_bucket_names) > 0:
        for bucket_name in middle_bucket_names:
            folders.append(os.path.join(base_dir_37, bucket_name)) 

        #print(f"Middle buckets: {folders}")

        for folder in folders:
            parquet_file_path = os.path.join(base_dir_37, folder, "clinvar.parquet")
            if os.path.exists(parquet_file_path):

                query = f"""
                    SELECT *
                    FROM "{parquet_file_path}"
                    WHERE Variant_Type == 'copy number loss' OR Variant_Type == 'deletion'
                """    

                results = conn.execute(query).fetch_df()

                if results.empty is False:
                    agg_results_df = pd.concat([agg_results_df, results], ignore_index=True)

            else:
                print(f"File does not exist: {parquet_file_path}")
    else:
        print("No middle buckets to process.")

    return agg_results_df




def search_lower_bound_bucket(conn, start_pos, stop_pos, base_dir_37, lower_bound_bucket_name)-> pd.DataFrame:
    print (f"start_pos: {start_pos}")
    print (f"stop_pos: {stop_pos}")

    parquet_file_path = os.path.join(base_dir_37, lower_bound_bucket_name, "clinvar.parquet")
    print (f"lower_bucket: {parquet_file_path}")

    if os.path.exists(parquet_file_path):
        query = f"""
            SELECT *
            FROM "{parquet_file_path}"
            CROSS JOIN UNNEST(Host_Genes) AS t(gene)
            WHERE Variant_Type == 'copy number loss' OR Variant_Type == 'deletion'
            AND gene.location.start = {start_pos} 
            AND gene.location.stop = {stop_pos}
        """
        results = conn.execute(query).fetch_df()    
        if results.empty is False:
            #print (f"Lower bucket results: {results}")
            return results
        else:
            print ("No results found in the lower bucket.")
            return None
    else:   
        print(f"Lower bucket file does not exist: {parquet_file_path}")
        return None



def search_higher_bound_bucket(conn, start_pos, stop_pos, base_dir_37, higher_bound_bucket_name)-> pd.DataFrame:
    print (f"start_pos: {start_pos}")
    print (f"stop_pos: {stop_pos}")

    parquet_file_path = os.path.join(base_dir_37, higher_bound_bucket_name, "clinvar.parquet")
    print (f"higher_bucket: {parquet_file_path}")

    if os.path.exists(parquet_file_path):
        query = f"""
            SELECT *
            FROM "{parquet_file_path}"
            CROSS JOIN UNNEST(Host_Genes) AS t(gene)
            WHERE Variant_Type == 'copy number loss' OR Variant_Type == 'deletion'
            AND gene.location.start = {start_pos} 
            AND gene.location.stop = {stop_pos}
        """
        results = conn.execute(query).fetch_df()    
        if results.empty is False:
            #print (f"Lower bucket results: {results}")
            return results
        else:
            print ("No results found in the lower bucket.")
            return None
    else:   
        print(f"Lower bucket file does not exist: {parquet_file_path}")
        return None




def main():
    print ("Start searching for variants...")

    start = 200179477
    end = 210880401
    chromosome = 2
    conn = duckdb.connect(database=':memory:')


    base_dir_37 = f"/home/davidmai/source/genoxus/GenoxusAnnotationRelease/GRCh=37/chr={chromosome}"
    print (f"base_dir_37: {base_dir_37}")


    lower_bound_bucket_name, middle_bucket_names, upper_bound_bucket_name, start_base, end_base = calculate_buckets(start=start, end=end)
    print (f"lower_bound_bucket_name: {lower_bound_bucket_name}")
    print (f"middle_bucket_names: {middle_bucket_names}")
    print (f"upper_bound_bucket_name: {upper_bound_bucket_name}")
    print (f"start_base: {start_base}")
    print (f"end_base: {end_base}")


    
    if len(middle_bucket_names):
        agg_results_df = search_middle_buckets(conn, base_dir_37, middle_bucket_names)
        print (f"agg_results_df: {len(agg_results_df)}")

        if len(agg_results_df) > 0:
            agg_findings_df = parse_buckets_results(agg_results_df)
            if agg_findings_df is not None and agg_findings_df.empty is False:
                print (f"agg_findings_df: {len(agg_findings_df)}")
            else:
                print ("No findings to report from the middle buckets results.")
        else:
            print ("No results found in the middle buckets.")
    else:
        print ("No middle buckets to search.")
    



    low_bucket_results_df = search_lower_bound_bucket(conn=conn, start_pos=start, stop_pos=start_base, base_dir_37=base_dir_37, lower_bound_bucket_name=lower_bound_bucket_name)
    low_bucket__findings_df = parse_buckets_results(low_bucket_results_df)
    if low_bucket__findings_df is not None and low_bucket__findings_df.empty is False:
        print (f"agg_findings_df from lower bucket: {len(low_bucket__findings_df)}")
        print (low_bucket__findings_df)
    else:
        print ("No findings to report from the lower bucket results.")




    high_results_df = search_higher_bound_bucket(conn=conn, start_pos=end_base, stop_pos=end, base_dir_37=base_dir_37, higher_bound_bucket_name=upper_bound_bucket_name)
    high_bucket_findings_df = parse_buckets_results(high_results_df)
    if high_bucket_findings_df is not None and high_bucket_findings_df.empty is False:
        print (f"agg_findings_df from higher bucket: {len(high_bucket_findings_df)}")
        print (high_bucket_findings_df)
    else:
        print ("No findings to report from the higher bucket results.")



    if agg_findings_df.empty is False:
        if low_bucket__findings_df is not None:
            agg_findings_df = pd.concat([agg_findings_df, low_bucket__findings_df], ignore_index=True)

        if high_bucket_findings_df is not None:
            agg_findings_df = pd.concat([agg_findings_df, high_bucket_findings_df], ignore_index=True)

    else:
        if low_bucket__findings_df is not None:
            agg_findings_df = low_bucket__findings_df

            if high_bucket_findings_df is not None:
                agg_findings_df = pd.concat([agg_findings_df, high_bucket_findings_df], ignore_index=True)

        elif high_bucket_findings_df is not None:
            agg_findings_df = high_bucket_findings_df
        else:
            print ("No results found in any of the buckets.")
            agg_findings_df = pd.DataFrame() # empty dataframe

    
    if agg_findings_df.empty is False:
        agg_findings_df.drop_duplicates(inplace=True)
        agg_findings_df.to_csv('agg_findings_df.csv', index=False)


    conn.close()
    print ("Search is finished, exit now.")



if __name__ == "__main__":
    main()
