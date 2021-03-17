import csv

def ExportPI_ImportDNAC(PI_file):

    with open(PI_file + '.csv',"r") as csv_file:
        line_count = 0
        csv_reader= csv.reader(csv_file, delimiter=',')
        with open("IMPORT_DNAC.csv","w") as csv_file_2:
            csv_writer= csv.writer(csv_file_2, delimiter=',')
            for line in csv_reader:
                if line_count == 0:
                    csv_writer.writerow( (line[0], line[2], line[3], line[4], line[5], line[6], line[7], line[9], line[11],
                    line[12], line[13], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23],
                    line[24], line[25], line[26], 'netconf_port' , 'isdevicecompute' , 'http_auth_method' , 'http_scheme' ,
                    'device_model_category', line[10], 'meraki_organization_id') )
                elif line_count >= 1:
                    csv_writer.writerow( (line[0], line[2], line[3], line[4], line[5], line[6], line[7], line[9], line[11],
                    line[12], line[13], line[15], line[16], line[17], line[18], line[19], line[20], line[21], line[22], line[23],
                    line[24], line[25], line[26], '' , '' , '' , '' , '', line[10], '') )
                line_count+=1
                print('Generating line:', line_count)
            print('FILE GENERATED: IMPORT_DNAC.csv')

set_ExportPI = input("Enter the PI generated file name (don't include .csv): ")
run = ExportPI_ImportDNAC(set_ExportPI)