def index_chopper(item, max_amount=1000):
    # adjusts piece number to reflect index in list
    # pass max_amount to cap index --- default: 1000

    while True:
        value = input('Which {} would you like to get? Enter a number 1-{}\n'.format(item, max_amount))
        try:
            list_index = int(value) - 1
        except ValueError:
            print('Invalid input.\n' * 1)
            continue

        if list_index >= max_amount:
            print("You don't have that many {}s!".format(item))
            print("Nobody does!\n")
            continue
        else:
            return list_index

