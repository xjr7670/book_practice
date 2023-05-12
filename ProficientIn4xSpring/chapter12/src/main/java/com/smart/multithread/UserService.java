package com.smart.multithread;

import com.smart.nestcall.BaseService;
import com.smart.nestcall.ScoreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service("userService")
public class UserService extends BaseService {
    private JdbcTemplate jdbcTemplate;
    private ScoreService scoreService;

    @Autowired
    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Autowired
    public void setScoreService(ScoreService scoreService) {
        this.scoreService = scoreService;
    }

    public void logon(String userName) {
        System.out.println("before userService.updateLastLogonTime method...");
        updateLastLogonTime(userName);
        System.out.println("after userService.updateLastLogonTime method...");

        // 1 在同一个线程中调用 scoreService#addScore()，将运行在同一个事务中
        // scoreService.addScore(userName, 20);

        // 2 在一个新线程中执行 scoreService#addScore()，将启动一个新的事务
        Thread myThread = new MyThread(this.scoreService, userName, 20);
        myThread.start();
    }

    public void updateLastLogonTime(String userName) {
        String sql = "UPDATE t_user u SET u.last_logon_time = ? WHERE user_name = ?";
        jdbcTemplate.update(sql, System.currentTimeMillis(), userName);
    }

    // 3 负责执行 scoreService#addScore() 的线程类
    private class MyThread extends Thread {
        private ScoreService scoreService;
        private String userName;
        private int toAdd;
        private MyThread(ScoreService scoreService, String userName, int toAdd) {
            this.scoreService = scoreService;
            this.userName = userName;
            this.toAdd = toAdd;
        }

        public void run() {
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("before scoreService.addScore method...");
            scoreService.addScore(userName, toAdd);
            System.out.println("after scoreService.addScore method...");
        }
    }
}
