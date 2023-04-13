package com.smart.service;

import java.util.ArrayList;
import java.util.List;

public class PostDao {
    private List<String> posts = new ArrayList<>();
    public void addPost(String post) {
        this.posts.add(post);
    }
}
