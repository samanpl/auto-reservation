from auto_reservation_ik.menu import show_menu
from auto_reservation_ik.utils.logger import log

def main():
    try:
        # target_time = input("Enter the booking time (HH:MM): ").strip()
        
        
        # scheduler.wait_until(target_time)

        # token = auth.authenticate()
        # booking.book_service(token)

        while True:
            choice = show_menu()

            # if choice == "1":
            #     from app.direct_reservation import direct_table_reservation
            #     direct_table_reservation()
            # elif choice == "2":
            #     from app.direct_activation import direct_table_activation
            #     direct_table_activation()
            # elif choice == "3":
            #     from app.scheduling import scheduling
            #     scheduling()
            # elif choice == "4":
            #     from app.task_management import task_management
            #     task_management()
            if choice == "5":
                from auto_reservation_ik.test import run_test
                run_test()
            elif choice == "0":
                log('goodbye!')
                return
            else:
                print("Invalid choice. Please select a valid option.")

    except Exception as e:
        log(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
