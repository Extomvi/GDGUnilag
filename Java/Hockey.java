/* Hockey extending Sports interface */
// Connects with the Sports.java file

public interface Hockey extends Sports {
    public void homeGoalScored();
    public void visitingTeamScored();
    public void endOfPeriod(int period);
    public void overtimePeriod(int ot);
}