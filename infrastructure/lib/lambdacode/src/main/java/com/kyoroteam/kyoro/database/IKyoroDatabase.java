package com.kyoroteam.kyoro.database;

import java.util.Date;
import java.util.Dictionary;
import java.util.List;

import com.kyoroteam.kyoro.tokenizer.KyoroTokenizeResult;

public interface IKyoroDatabase {
    void initalDatabaseSetup();

    void updateSourceContent(String sourceName, List<KyoroTokenizeResult> updates);

    Dictionary<String, Date> getSourceLastUpdatedTimes();
}
