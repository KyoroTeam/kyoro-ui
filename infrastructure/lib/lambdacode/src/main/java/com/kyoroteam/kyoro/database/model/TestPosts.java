package com.kyoroteam.kyoro.database.model;

import java.sql.*;
import javax.persistence.*;
import lombok.Data;

@Data
@Entity(name = "com.kyoroteam.kyoro.database.model.TestPosts")
@Table(name = "test_posts")
public class TestPosts {

  @Id
  @Column(name = "\"test_posts_tid\"", nullable = true)
  private Integer testPostsTid;
  @Column(name = "\"test_tid\"", nullable = true)
  private Integer testTid;
}