package com.kyoroteam.kyoro;

import java.nio.file.NoSuchFileException;

import com.google.gson.Gson;
import com.kyoroteam.kyoro.management.Manager;

public class Main {
    public static void main(String[] args) {
        main(args, System.out);
    }

    public static void main(String[] args, java.io.PrintStream outStream) {
        try {
            if (args.length != 1) {
                throw new Exception("Filename must be specified as first argument");
            }

            var manager = new Manager();
            var results = manager.tokenizeFileContent(args[0]);

            var gson = new Gson();
            String json = gson.toJson(results);
            outStream.print(json);
        } catch (NoSuchFileException ex) {
            var error = new Error("No such file: " + ex.getMessage());
            outStream.println(new Gson().toJson(error));
        } catch (Exception ex) {
            var error = new Error(ex.getMessage());
            outStream.println(new Gson().toJson(error));
        }
    }
}
