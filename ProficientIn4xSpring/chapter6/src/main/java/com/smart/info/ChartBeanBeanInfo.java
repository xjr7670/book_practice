package com.smart.info;

import javafx.scene.chart.Chart;

import java.beans.IntrospectionException;
import java.beans.PropertyDescriptor;
import java.beans.SimpleBeanInfo;

public class ChartBeanBeanInfo extends SimpleBeanInfo {
    public PropertyDescriptor[] getProgertyDescriptors() {
        try {
            PropertyDescriptor titlePositionDescriptor = new PropertyDescriptor("titlePosition", ChartBean.class);
            titlePositionDescriptor.setPropertyEditorClass(TitlePositionEditor.class);

            PropertyDescriptor inverseDescriptor = new PropertyDescriptor("inverse", ChartBean.class);
            inverseDescriptor.setPropertyEditorClass(InverseEditor.class);
            return new PropertyDescriptor[] {titlePositionDescriptor, inverseDescriptor};
        } catch (IntrospectionException e) {
            e.printStackTrace();
            return null;
        }
    }
}
