package sample.dbunit;

import org.unitils.core.Module;
import org.unitils.core.TestListener;

import java.lang.reflect.Method;

public class CustomExtModule implements Module {
    public TestListener getTestListener() {
        return new CustomExtListener();
    }

    protected class CustomExtListener extends TestListener {
        @Override
        public void afterTestMethod(Object testObject, Method testMethod, Throwable testThrowable) {
            // todo..
        }

        @Override
        public void beforeTestMethod(Object testObject, Method testMethod) {
            //todo..
        }
    }
}
