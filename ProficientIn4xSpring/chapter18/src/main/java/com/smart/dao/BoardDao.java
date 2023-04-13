package com.smart.dao;

import com.smart.domain.Board;

import java.util.Iterator;

public class BoardDao extends BaseDao<Board> {
    private static final String GET_BOARD_NUM = "select count(f.boardId) from Board f";

    // 获取论坛板块数目的方法
    public long getBoardNum() {
        Iterator iter = getHibernateTemplate().iterate(GET_BOARD_NUM);
        return ((Long) iter.next());
    }
}
