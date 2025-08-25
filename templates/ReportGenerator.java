import java.util.Random;

public class ReportGenerator {
    public static void main(String[] args) {
        System.out.println("Generating medical report...");
        Random rand = new Random();
        int id = rand.nextInt(10000);  // Random number between 0 and 9999
        System.out.println("Report ID: " + id);
        System.out.println("Status: Completed.");
    }
}
