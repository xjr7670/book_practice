package com.smart.info;

import javax.swing.*;

import static javax.swing.SwingConstants.CENTER;

public class ChartBean extends JPanel {
    private int titlePosition = CENTER;
    private boolean inverse;

    public void setInverse(boolean inverse) {
        this.inverse = inverse;
    }

    public boolean getInverse() {
        return this.inverse;
    }
}
