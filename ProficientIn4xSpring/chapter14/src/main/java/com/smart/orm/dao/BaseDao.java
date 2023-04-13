package com.smart.orm.dao;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate5.HibernateTemplate;

import java.io.Serializable;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;

public class BaseDao<T> {       // 1 提供 DAO 类级别的泛型支持

    @Autowired
    private HibernateTemplate hibernateTemplate;        // 2 注入 Hibernate 模板类

    private Class entiryClass;      // 3 DAO 的泛型类，即子类所指定的 T 所对应的类型

    public BaseDao() {              // 4 通过反射方式获取子类 DAO 对应的泛型实体类
        Type getType = getClass().getGenericSuperclass();
        Type[] params = ((ParameterizedType) getType).getActualTypeArguments();
        entiryClass = (Class) params[0];
    }

    public T get(Serializable id) {
        return (T) hibernateTemplate.get(entiryClass, id);      // 5 直接使用 entityClass
    }

    public void save(T entity) {
        hibernateTemplate.save(entity);
    }

    public void update(T entity) {
        hibernateTemplate.update(entity);
    }

    public HibernateTemplate getHibernateTemplate() {
        return hibernateTemplate;
    }
}
