from utils import reports as r, files as f, settings as s, validations as v

def add_new_donator(donator, donation_dictionary):
    donation_dictionary.update({donator : []})
    return donation_dictionary

def add_new_donation(donor, donation_dictionary, donation):
    donation_dictionary[donor].append(donation)
    return donation_dictionary

def get_email(donor, donation):
    email = f"""Dear {donor},
        Thank you for donating $ {donation} to our foundation.
    Kind regards,
    Local Charity Staff"""
    return email

def print_email(donor, donation):
    print("Email to copy:\n---------------")
    print(get_email(donor, donation))
    print("---------------")

def get_donor_from_input():
    while True:
        donor = input("Please enter donor full name or type 'list': ").strip()
        if v.is_full_name(donor):
            break
        else:
            print("The inserted value is wrong. Pease enter donor name: ")
            continue
    return donor

def get_donation_from_input():
    while True:
        donation = input("Enter the donation amount: ").strip()
        try:
            donation = float(donation)
        except ValueError:
                pass
        finally:
            if v.is_money(donation):
                break
            else:
                print("The inserted value is wrong. Pease enter money value: ")
                continue
    return donation

def send_thanks():
    donation_dictionary = r.get_donation_dictionary()
    donor_list = donation_dictionary.keys()
    donor = get_donor_from_input()
    if donor == 'list':
        r.print_donor_list(donor_list)
    else:
        if donor not in donor_list:
            donation_dictionary = add_new_donator(donor, donation_dictionary)
        donation = get_donation_from_input()
        donation_dictionary = add_new_donation(donor, donation_dictionary, donation)
        print_email(donor, donation)
        f.write_to_json(donation_dictionary, s.DONATIONS_PATH)

    
