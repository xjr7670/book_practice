package ch6.v2;

import org.apache.hadoop.io.Text;

public class NcdcRecordParser {
    private static final int MISSING_TEMPERATURE = 9999;

    private String year;
    private int airTemperature;
    private String quality;
    private byte[] stationId;

    public void parse(String record) {
        year = record.substring(15, 19);
        String airTemperatureString;
        // Remove leading plus sign as parseInt doesn't like them (pre-Java 7)
        if (record.charAt(87) == '+') {
            airTemperatureString = record.substring(88, 92);
        } else {
            airTemperatureString = record.substring(87, 92);
        }
        airTemperature = Integer.parseInt(airTemperatureString);
        quality = record.substring(92, 93);
    }

    public void parse(Text record) {
        parse(record.toString());
    }

    public boolean isValidTemperature() {
        return airTemperature != MISSING_TEMPERATURE && quality.matches("[01459]");
    }

    public String getYear() {
        return year;
    }

    public int getAirTemperature() {
        return airTemperature;
    }

    public boolean isMalformedTemperature() {  // 书中没有给出这个方法的实现，但是在 v4 版本中却直接使用了。这里是我乱加的
        return airTemperature == MISSING_TEMPERATURE;
    }

    public byte[] getStationId() {
        return stationId;
    }

    public void setStationId(byte[] stationId) {
        this.stationId = stationId;
    }

    public boolean isMissingTemperature() {
        return airTemperature == MISSING_TEMPERATURE;
    }

    public String getQuality() {
        return this.quality;
    }

    public int getYearInt() {
        return Integer.parseInt(this.year);
    }
}
