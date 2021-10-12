package com.kyoroteam.kyoro;

import com.google.gson.Gson;
import com.kyoroteam.kyoro.management.Manager;

public class Main {
    public static void main(String[] args) {
        try {
            var manager = new Manager();
            var results = manager.tokenizeContent(args[0]);
            var gson = new Gson();
            String json = gson.toJson(results);
            System.out.print(json);
        } catch (Exception ex) {
            System.err.println(ex.getMessage());
        }
    }
}
