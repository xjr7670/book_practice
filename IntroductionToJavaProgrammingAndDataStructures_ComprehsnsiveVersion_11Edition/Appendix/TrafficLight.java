public enum TrafficLight {
    RED ("PLEASE STOP"), GREEN ("PLEASE GO"),
    YELLOW ("PLEASE CAUTION");

    private String description;

    private TrafficLight(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}