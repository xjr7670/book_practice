package sample.hibernate;

import com.smart.dao.UserDao;
import com.smart.dao.hibernate.WithoutSpringUserDaoImpl;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import org.unitils.orm.hibernate.HibernateUnitils;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

public class SimpleUserDaoTest extends BaseDaoTest {
    private UserDao userDao;

    @BeforeClass
    public void init() {
        userDao = new WithoutSpringUserDaoImpl();
        //userDao.setSessionFactory(sessionFactory);
    }

    @Test
    public void testMappingToDatabase() {
        HibernateUnitils.assertMappingWithDatabaseConsistent();
    }

    @Test
    public void testUserDao() {
        assertNotNull(userDao);
        assertNotNull(userDao.findUserByUserName("tom"));
        assertEquals("tom", userDao.findUserByUserName("tom").getUserName());
    }
}
