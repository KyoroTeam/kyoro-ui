package com.kyoroteam.kyoro;

import com.google.gson.Gson;
import com.kyoroteam.kyoro.management.Manager;

public class Main {
    public static void main(String[] args) {
        try {
            var manager = new Manager();
            var results = manager.tokenizeFileContent("/home/james/Desktop/datasmall.txt");
            var gson = new Gson();
            String json = gson.toJson(results);
            System.out.print(json);
        } catch (Exception ex) {
            System.err.println(ex.getMessage());
        }
    }
}
