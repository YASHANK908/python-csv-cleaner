import csv
from datetime import datetime

import logging



logging.basicConfig(
    filename="cleaner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_email(email):
    has_at = "@" in email
    has_com = email.endswith(".com")
    one_at = email.count("@") == 1

    return has_at and has_com and one_at


def is_incomplete(row):
    return any(val.strip() == "" for val in row)


def generate_report( total_records,data_quality_percentage,incomplete_percentage,incomplete_records,complete_records,valid_emails,invalid_emails, duplicate_emails,malformed_rows,valid_email_percentage,duplicate_email_percentage,unique_emails,unique_email_percentage, total_emails,processing_status ):
    with open("reports/cleaning_report.txt", "w",encoding="utf-8") as file:
       file.write("CUSTOMER DATA QUALITY REPORT\n")
       file.write("----------------------------\n\n")
   
       file.write("report date:"+str(datetime.now().strftime("%d-%m-%Y ") )+"\n")
   
       file.write("report time:"+str(datetime.now().strftime("%H:%M:%S") )+"\n")
   
       file.write("Total records: " + str(total_records) + "\n")
       file.write("Incomplete records: " + str(incomplete_records) + "\n")
       file.write("complete records: " + str(complete_records) + "\n")
       file.write(f"Total Emails:{total_emails}\n")
       file.write("Valid emails: " + str(valid_emails) + "\n")
       file.write("Invalid emails: " + str(invalid_emails) + "\n")
       file.write("Duplicate emails: " + str(duplicate_emails) + "\n\n")
       file.write("Malformed Rows :"+str(malformed_rows)+"\n\n")
       file.write(f"Data Quality Percentage :{data_quality_percentage:.2f}%\n")
       file.write(f"Incomplete Percentage :{incomplete_percentage:.2f}%\n")
       file.write(f"valid Email Percentage :{valid_email_percentage:.2f}%\n")
       file.write(f"Duplicate Email Percentage :{duplicate_email_percentage:.2f}%\n")
       file.write(f"Unique Emails:{unique_emails}\n")
       file.write(f"Unique Email Percentage :{unique_email_percentage:.2f}%\n")
       file.write(f"Processing Status:{processing_status}\n")
       

   
       file.write("Report generated successfully.\n")
   
    logging.info("CSV Report Generated")




def process_csv():
    total_records = 0
    data_quality_percentage=0
    incomplete_percentage=0
    incomplete_records = 0
    complete_records=0
    valid_emails = 0
    invalid_emails = 0
    duplicate_emails = 0
    malformed_rows=0
    valid_email_percentage=0
    duplicate_email_percentage=0
    unique_emails=0
    unique_email_percentage = 0
    total_emails=0
    processing_status="SUCCESS"
    seen_emails = set()



    file_path=input("Enter The File Path")
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        logging.info("CSV Processing started")

        reader = csv.reader(file)
        header = next(reader,None)
        if header is None:
            processing_status="FAILED"
            logging.error("Error: customers.csv is empty.")
             
            return (
    total_records,
    data_quality_percentage,
    incomplete_percentage,
    incomplete_records,
    complete_records,
    valid_emails,
    invalid_emails,
    duplicate_emails,
    malformed_rows,
    valid_email_percentage,
    duplicate_email_percentage,
    unique_emails,
    unique_email_percentage,
    total_emails,
    processing_status
)

        for row in reader:
            total_records += 1
            if len(row)!=4:
                malformed_rows+=1
                continue
           

            if is_incomplete(row):
                incomplete_records += 1
            else:
                complete_records+=1

            email = row[2].strip().lower()

            if email:
                if validate_email(email):
                    valid_emails += 1
                else:
                    invalid_emails += 1

                if email in seen_emails:
                    duplicate_emails += 1
                else:
                    seen_emails.add(email)

        if total_records == 0:
            processing_status = "FAILED"
            logging.error("CSV contains no customer records")            

        unique_emails = len(seen_emails)
        valid_structure_records=total_records-malformed_rows
        total_emails=valid_emails+invalid_emails
        if total_emails>0:
            valid_email_percentage=(valid_emails/total_emails)*100
            duplicate_email_percentage=((duplicate_emails/total_emails))*100
            unique_email_percentage = (unique_emails/total_emails)*100
        else:
            valid_email_percentage=0
            duplicate_email_percentage=0
            unique_email_percentage=0
        if valid_structure_records>0:
            data_quality_percentage=(complete_records/valid_structure_records)*100
            incomplete_percentage=(incomplete_records/valid_structure_records)*100
        else:
            data_quality_percentage=0
            incomplete_percentage=0

        logging.info("CSV Processing Completed")

    return (
        total_records,
        data_quality_percentage,
        incomplete_percentage,
        incomplete_records,
        complete_records,
        valid_emails,
        invalid_emails,
        duplicate_emails,
        malformed_rows,
        valid_email_percentage,
        duplicate_email_percentage,
        unique_emails,
        unique_email_percentage,
        total_emails,
        processing_status
    )
    
     
     
def main():
    try:
        results = process_csv()
        if results is not None:
            generate_report(*results)
            if results[14]=="FAILED":
                print("CSV PROCESSING FAILED")
                print("Reason: customers.csv is empty.")
            else:
                 print("="*40)
                 print("          CSV Cleaner APPLICATION")
                 print("="*40)
                 print("CSV CLEANING SUMMARY")
                 print("--------------------")
                
                 print(f"Total Records: {results[0]}")
                 print(f"Complete Records: {results[4]}")
                 print(f"Incomplete Records: {results[3]}")
                 print(f"Malformed Rows: {results[8]}")
                 print(f"Data Quality: {results[1]:.2f}%")
                 print(f"Incomplete Percentage:{results[2]:.2f}%")
                 print(f"Total Emails:{results[13]}")
                 print(f"Valid Email Percentage:{results[9]:.2f}%")
                 print(f"Duplicate Email Percentage:{results[10]:.2f}%")
                 print(f"Unique Emails:{results[11]}")
                 print(f"Unique Email Percentage:{results[12]:.2f}%")
                 print(f"Processing Status:{results[14]}")
                           

        
           


    except FileNotFoundError:
        logging.error("customers.csv file not found")
        print("Error: customers.csv file not found.")

if __name__ == "__main__":
    main()

 