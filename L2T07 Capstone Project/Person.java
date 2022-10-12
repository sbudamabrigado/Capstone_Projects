
public class Person {
	// Declaring Class properties
	String person_type;
	String person_name;
	String person_telephone;
	String person_email;
	String person_address;
	String project_number;
	
	// Creating Constructor for Person Class
	public Person(String person_type, String person_name, String person_telephone, String person_email, String person_address, String project_number){
		this.person_type = person_type;
		this.person_name = person_name;
		this.person_telephone = person_telephone;
		this.person_email = person_email;
		this.person_address = person_address;
		this.project_number = project_number;
	}
	
	// Declare method to return object as string
	public String toString() {
		String objectToString = "Type: " + person_type + "\n Name: " + person_name + "\nTelephone: " + person_telephone + "\nEmail: " + person_email + "\nAddress: " + person_address + "\nProject Number: " + project_number;
		return objectToString;
	}
	
	// Declare method to update contact details
	public void updateContactDetails(String new_telephone, String new_email) {
		person_telephone = new_telephone;
		person_email = new_email;
	}
	
}
