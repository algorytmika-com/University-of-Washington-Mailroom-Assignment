from utils import files as f, settings as s

def get_donation_dictionary():
    dictionary = f.read_from_json(s.DONATIONS_PATH)
    return dictionary

def get_donor_list():
    dictionary = f.read_from_json(s.DONATIONS_PATH)
    return sorted(dictionary.keys())

def print_donor_list(donor_list):
    if donor_list:
        print('The donor list:')
        for donor in donor_list:
            print(donor)        
    else:
        print('The donor list is empty:')

def get_donations_aggregated_list(donation_dictionary):
    donation_aggregated_dict = {}
    donation_aggregated_list = []
    for donor in donation_dictionary:
        donation_sum = sum(donation_dictionary[donor])
        donation_num = len(donation_dictionary[donor])
        donation_avg = donation_sum / donation_num
        donation_aggregated_dict.update({donor : {"sum" : donation_sum, "num" : donation_num, "avg" : donation_avg}})
    donation_aggregated_list = sorted(donation_aggregated_dict.items(), 
                                            key = lambda x : x[1]['sum'], reverse=True)
    return donation_aggregated_list

def get_formatted_report(donation_aggregated_list):
    col1 = "Donor name"
    col2 = " Total Given "
    col3 = " Num Gifts "
    col4 = " Average Gift"
    formatted = f"{col1:20}|{col2:12}|{col3:12}|{col4:12}\n"
    for row in donation_aggregated_list:
        col1_len = ':20'
        formatted = formatted + f"{row[0]:20} ${row[1]['sum']:12.2f}{row[1]['num']:12d}  ${row[1]['avg']:12.2f}\n" 
    return formatted

def create_report():
    donation_aggregated_list = get_donations_aggregated_list(get_donation_dictionary())
    formatted_report = get_formatted_report(donation_aggregated_list)
    print(formatted_report)





