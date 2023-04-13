package com.smart.dao;

import org.hibernate.Query;
import org.hibernate.Session;
import org.springframework.util.Assert;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate5.HibernateTemplate;

import java.io.Serializable;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BaseDao<T> {
    private Class<T> entityClass;
    @Autowired
    private HibernateTemplate hibernateTemplate;

    // 通过反射获取子类确定的泛型类
    public BaseDao() {
        Type genType = getClass().getGenericSuperclass();
        Type[] params = ((ParameterizedType) genType).getActualTypeArguments();
        entityClass = (Class) params[0];
    }

    // 根据 ID 加载 PO 实例
    public T load(Serializable id) {
        return (T) getHibernateTemplate().load(entityClass, id);
    }

    // 根据 ID 获取 PO 实例
    public T get(Serializable id) {
        return (T) getHibernateTemplate().get(entityClass, id);
    }

    // 获取 PO 的所有对象
    public List<T> laodAll() {
        return getHibernateTemplate().loadAll(entityClass);
    }

    // 保存 PO
    public void save(T entity) {
        getHibernateTemplate().save(entity);
    }

    // 删除 PO
    public void remove(T entity) {
        getHibernateTemplate().delete(entity);
    }

    // 更改 PO
    public void update(T entity) {
        getHibernateTemplate().update(entity);
    }

    // 执行 HQL 查询
    public List find(String hql) {
        return this.getHibernateTemplate().find(hql);
    }

    // 执行带参数的 HQL 查询
    public List find(String hql, Object... params) {
        return this.getHibernateTemplate().find(hql, params);
    }

    // 对延迟加载的实体 PO 进行初始化
    public void inittialize(Object entity) {
        this.getHibernateTemplate().initialize(entity);
    }

    public HibernateTemplate getHibernateTemplate() {
        return hibernateTemplate;
    }

    @Autowired
    public void setHibernateTemplate(HibernateTemplate hibernateTemplate) {
        this.hibernateTemplate = hibernateTemplate;
    }

    // 分页查询函数，使用 HQL
    public Page pageQuery(String hql, int pageNo, int pageSize, Object... values) {
        Assert.hasText(hql);
        Assert.isTrue(pageNo >= 1, "pageNo should start from 1");
        // Count 查询
        String countQueryString = "select count(*) " + removeSelect(removeOrders(hql));
        List countlist = getHibernateTemplate().find(countQueryString, values);
        long totalCount = (Long) countlist.get(0);

        if (totalCount < 1) {
            return new Page();
        }
        // 实际查询返回分页对象
        int startIndex = Page.getStartOfPage(pageNo, pageSize);
        Query query = createQuery(hql, values);
        List list = query.setFirstResult(startIndex).setMaxResults(pageSize).list();
        return new Page(startIndex, totalCount, pageSize, list);
    }

    // 创建 Query 对象
    public Query createQuery(String hql, Object... values) {
        Assert.hasText(hql);
        Query query = getSession().createQuery(hql);
        for (int i = 0; i < values.length; i++) {
            query.setParameter(i, values[i]);
        }
        return query;
    }

    // 去除 HQL 的 select 子句
    private static String removeSelect(String hql) {
        Assert.hasText(hql);
        int beginPos = hql.toLowerCase().indexOf("form");
        Assert.isTrue(beginPos != -1, " hql : " + hql + " must has a keyword 'form'");
        return hql.substring(beginPos);
    }

    // 去除 HQL 的 orderby 子句
    private static String removeOrders(String hql) {
        Assert.hasText(hql);
        Pattern p = Pattern.compile("order\\s*by[\\w|\\W|\\s|\\S]*", Pattern.CASE_INSENSITIVE);
        Matcher m = p.matcher(hql);
        StringBuffer sb = new StringBuffer();
        while (m.find()) {
            m.appendReplacement(sb, "");
        }
        m.appendTail(sb);
        return sb.toString();
    }

    public Session getSession() {
        return hibernateTemplate.getSessionFactory().getCurrentSession();
    }
}
