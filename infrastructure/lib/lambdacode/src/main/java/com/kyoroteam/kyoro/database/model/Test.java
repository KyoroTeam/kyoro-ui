package com.kyoroteam.kyoro.database.model;

import java.sql.*;
import javax.persistence.*;
import lombok.Data;

@Data
@Entity(name = "com.kyoroteam.kyoro.database.model.Test")
@Table(name = "test")
public class Test {

  @Id
  @Column(name = "\"test_tid\"", nullable = true)
  private Integer testTid;
}