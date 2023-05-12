package sample.hibernate;

import org.hibernate.SessionFactory;
import org.testng.annotations.Test;
import org.unitils.UnitilsTestNG;
import org.unitils.orm.hibernate.annotation.HibernateSessionFactory;

import static org.testng.Assert.assertNotNull;

@HibernateSessionFactory("hibernate.cfg.xml")
public class BaseDaoTest extends UnitilsTestNG {
    @HibernateSessionFactory
    public SessionFactory sessionFactory;

    public void setSessionFactory(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    public SessionFactory getSessionFactory() {
        return this.sessionFactory;
    }

    @Test
    public void testSessionFactory() {
        assertNotNull(sessionFactory);
    }
}
