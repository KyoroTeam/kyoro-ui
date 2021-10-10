package com.kyoroteam.kyoro.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Date;
import java.util.Dictionary;
import java.util.List;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizeResult;

public class KyoroDatabase implements IKyoroDatabase {

    private Connection Connection;

    public KyoroDatabase(Connection connection) {
        Connection = connection;
    }

    @Override
    public void updateSourceContent(String sourceName, List<KyoroTokenizeResult> updates) {
        // TODO Auto-generated method stub
        try {
            var statement = Connection.createStatement();
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    @Override
    public Dictionary<String, Date> getSourceLastUpdatedTimes() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void initalDatabaseSetup() {
        // TODO Auto-generated method stub

    }

}
