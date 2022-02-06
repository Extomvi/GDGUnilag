/* Extending Sports interface into Football */

public interface Football extends Sports {
    public void homeTeamScored(int points);
    public void visitingTeamScored(int points);
    public void endOfQuater(int quater);
}