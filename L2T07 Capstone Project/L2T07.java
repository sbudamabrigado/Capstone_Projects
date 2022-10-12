import java.util.*;

public class L2T07 {
	
	public static void main(String[] args) {
		// Initializing objects
		Person person = null ;
		Project project = null;
		
		while (true) {
			// Declare Scanner for input from user
			Scanner input = new Scanner(System.in);
			
			// Display menu to user
			System.out.println("Please select an option:");
			System.out.println("\t(1) To capture details of new project\n\t(2) To change the due date of the project\n\t(3) To change the total amount of the fee paid to date\n\t(4) To update a contractor’s contact details\n\t(5) To finalise the project\n\t(6) Exit");
			int menu_option = input.nextInt();
			
			// Based on input decide what to do
			if(menu_option ==1) {
				// Generating Unique project number
				String project_number ="PRO" + new  Random().nextInt(1000,9999);
				
				// Requesting user input for project details
				System.out.print("Please enter project name: ");
				String project_name = input.next();
				System.out.print("Please enter project type: ");
				String project_type = input.next();
				System.out.print("Please enter location of project (address): ");
				String location_of_project = input.next();
				System.out.print("Please enter project ERF number: ");
				String project_ERF_number = input.next();
				System.out.print("Please enter project fee: ");
				double project_fee = input.nextDouble();
				System.out.print("Please enter amount paid to date for project: ");
				double project_amount_paid_to_date = input.nextDouble();
				System.out.print("Please enter project deadline: ");
				String project_deadline = input.next();
				
				// Requesting user input for person details
				System.out.print("Please enter person type: ");
				String person_type = input.next();
				System.out.print("Please enter person first name: ");
				String person_firstname = input.next();
				System.out.print("Please enter person last name: ");
				String person_lastname = input.next();
				System.out.print("Please enter person telephone: ");
				String person_telephone = input.next();
				System.out.print("Please enter person email: ");
				String person_email = input.next();
				System.out.print("Please enter person address: ");
				String person_address = input.next();
				
				// Based on input create class objects to capture the details
				// Check if project name was entered. if not enter project type + surname of customer
				if(project_name == null || project_name == "") {
					project_name = project_type + person_lastname;
					String person_name = person_firstname + person_lastname;
					
					// Creating Person object
					person = new Person(person_type, person_name, person_telephone, person_email, person_address, project_number);
					
					// Creating Project object
					project = new Project(project_number, project_name, project_type, location_of_project, project_ERF_number, project_fee, project_amount_paid_to_date, project_deadline, person);
					
					// Display success message
					System.out.println("\nDetails successfully Captured\n");
				}
				else {
					String person_name = person_firstname + person_lastname;
					
					// Creating Person object
					person = new Person(person_type, person_name, person_telephone, person_email, person_address, project_number);
					
					// Creating Project object
					project = new Project(project_number, project_name, project_type, location_of_project, project_ERF_number, project_fee, project_amount_paid_to_date, project_deadline, person);

					// Display success message
					System.out.println("\nDetails successfully Captured\n");
				}
			}
			else if(menu_option == 2) {
				System.out.print("Please enter new due date: ");
				String new_deadline = input.next();
				
				project.changeDeadline(new_deadline);
				
				// Display success message
				System.out.println("\nDate has successfully been changed\n");
			}
			else if(menu_option == 3) {
				System.out.print("Please enter new amount paid to date: ");
				double new_amount_paid_to_date = input.nextDouble();
				
				// Update Amount paid
				project.updateAmountPaidToDate(new_amount_paid_to_date);
				
				// Display success message
				System.out.println("\nAmount has been updated.\n");
			}
			else if(menu_option == 4) {
				//Check if there is a contractor
				if(person.person_type != "contractor") {
					System.out.println("Contractor not found or details have not been enterered for contractor");
				}
				else {
					// Get contractor details from user
					System.out.println("Please enter new details");
					System.out.print("\tTelephone: ");
					String new_telephone = input.next();
					System.out.print("\tEmail: ");
					String new_email = input.next();
					
					// Update contractor details
					person.updateContactDetails(new_telephone, new_email);
					
					// Display success message
					System.out.println("\nDetails have been successfully changed\n");
				}
			}
			else if(menu_option == 5) {
				// Check if project was paid for in full
				if(project.outstandingAmount() <= 0) {
					//Get completion date from user
					System.out.print("Please enter completion date: ");
					String completion_date = input.next();
					
					// Call Method to finalize project
					project.finalizeProject(completion_date);
					
					// Display success message
					System.out.println("Project successfully finalized");
				}else {
					// Call Method to Generate Invoice
					project.generateInvoice();
					
					// Get completion date from user
					System.out.print("Please enter completion date: ");
					String completion_date = input.next();
					
					// Call Method to finalize project
					project.finalizeProject(completion_date);
					
					//Display success message
					System.out.println("Project successfully finalized");
				}
			}
			else {
				System.out.println("GoodBye!!");
				break;
			}
		}
	}
}
