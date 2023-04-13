package com.smart.nestcall;

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

    // 1 该方法嵌套调用了本类的其他方法及其他服务类的方法
    public void logon(String userName) {
        System.out.println("before userService.updateLastLogonTime...");
        updateLastLogonTime(userName);
        System.out.println("after userService.updateLastLogonTime...");

        System.out.println("before scoreService.addScore...");
        scoreService.addScore(userName, 20);
        System.out.println("after scoreService.addScore...");
    }

    public void updateLastLogonTime(String userName) {
        String sql = "UPDATE t_user u SET u.last_logon_time = ? WHERE user_name = ?";
        jdbcTemplate.update(sql, System.currentTimeMillis(), userName);
    }
}
