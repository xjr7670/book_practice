package sample.unitils;

import com.smart.domain.User;
import org.testng.annotations.Test;
import org.unitils.reflectionassert.ReflectionAssert;
import org.unitils.reflectionassert.ReflectionComparatorMode;

import static org.unitils.reflectionassert.ReflectionAssert.assertLenientEquals;
import static org.unitils.reflectionassert.ReflectionAssert.assertReflectionEquals;
import static org.unitils.reflectionassert.ReflectionAssert.assertPropertyLenientEquals;

public class AssertReflectionEqualsTest {
    @Test
    public void testReflection() {
        User user1 = new User("tom", "1234");
        User user2 = new User("tom", "1234");

        assertReflectionEquals(user1, user2);
    }

    @Test
    public void testLenientEquals() {
        Integer orderList1[] = new Integer[]{1, 2, 3};
        Integer orderList2[] = new Integer[]{3, 2, 1};

        // 1 测试两个数组的值是否相等，忽略顺序
        assertReflectionEquals(orderList1, orderList2, ReflectionComparatorMode.LENIENT_ORDER);
        assertLenientEquals(orderList1, orderList2);

        // 2 测试两个对象的值是否相等，忽略默认值
        User user1 = new User("tom", "1234");
        User user2 = new User("tom", "1234");
        assertLenientEquals(user1, user2);
    }

    User user = new User("tom", "1234");
}
