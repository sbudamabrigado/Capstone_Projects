
public class Project {
	// Declaring Class properties
	String project_number; // Declared as string in case project number starts with pro e.g pro123032 
	String project_name;
	String project_type;
	String location_of_project;
	String project_ERF_number;
	double project_fee;
	double project_amount_paid_to_date;
	String project_deadline;
	Person person;
	String project_finalized;
	String completion_date;
	
	// Creating Constructor for Project Class
	public Project(String project_number, String project_name, String project_type, String location_of_project, String project_ERF_number, double project_fee, double project_amount_paid_to_date, String project_deadline,Person person) {
		this.project_number = project_number;
		this.project_name = project_name;
		this.project_type = project_type;
		this.location_of_project = location_of_project;
		this.project_ERF_number = project_ERF_number;
		this.project_fee = project_fee;
		this.project_amount_paid_to_date = project_amount_paid_to_date;
		this.project_deadline = project_deadline;
		this.person = person;
		this.project_finalized = "Not Yet Finalized";
	}
	
	// Declare method to return object as string
	public String toString() {
		String objectToString = "Project Number: "+ project_number+ "\nProject Name: " + project_name + "\nProject Type: " + project_type + "Location of project: " + location_of_project + "\nERF Number: " + project_ERF_number ;
		objectToString += "\nProject Fee: " + project_fee + "\nAmount paid to date: " + project_amount_paid_to_date + "\nProject Deadline: " + project_deadline;
		objectToString +="\n\n" + person.toString();
		return objectToString;		
	}
	
	// Declaring method to change the deadline of a project
	public void changeDeadline(String new_deadline) {
		project_deadline = new_deadline;
	}
	
	// Declaring method to change the amount paid to date
	public void updateAmountPaidToDate(double new_amount_paid_to_date) {
		project_amount_paid_to_date = new_amount_paid_to_date;
	}
	
	// Declare Method to check if project fee was paid in full
	public double outstandingAmount() {
		return project_fee - project_amount_paid_to_date;
	}
	
	// Declare method to finalize project
	public void finalizeProject(String completed_date) {
		project_finalized = "Finalised";
		completion_date = completed_date;
	}
	
	// Declare Method to generate invoice
	public void generateInvoice() {
		// Generate Invoice
		String invoice = "Customer Name: " + person.person_name + "\nCustomer Telephone: " + person.person_telephone + "\nCustomer Email: " + person.person_email;
		invoice +="\n\nDear valuable client please note the amount of " + outstandingAmount() + " due to us. \nProject name: " + project_name + "\nProject number: " + project_number;
		
		// Display Invoice
		System.out.println(invoice);
	}
	
	
}
