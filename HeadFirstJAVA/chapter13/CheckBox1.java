import java.awt.*;
import javax.swing.*;


public class CheckBox1 {
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        JPanel panel = new JPanel();

        JCheckBox check = new JCheckBox("Goes to 11");
        check.addItemListener(this);

        frame.getContentPane().add(BorderLayout.CENTER, panel);
        frame.getContentPane().add(BorderLayout.NORTH, check);

        frame.setSize(300, 250);
        frame.setVisible(true);
    }

    public void itemStateChanged(ItemEvent ev) {
        String onOrOff = "off";
        if (check.isSelected()) {
            onOrOff = "on";
        }
        System.out.println("Check box is " + onOrOff);
    }
}