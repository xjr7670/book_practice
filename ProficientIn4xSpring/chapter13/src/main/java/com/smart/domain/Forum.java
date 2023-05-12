package com.smart.domain;

public class Forum {
    private String forumName;
    private String forumDesc;
    private int forumId;

    public void setForumName(String forumName) {
        this.forumName = forumName;
    }
    public String getForumName() {
        return this.forumName;
    }

    public void setForumDesc(String forumDesc) {
        this.forumDesc = forumDesc;
    }
    public String getForumDesc() {
        return this.forumDesc;
    }

    public void setForumId(int forumID) {
        this.forumId = forumID;
    }
    public int getForumId() {
        return this.forumId;
    }
}
