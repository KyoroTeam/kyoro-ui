package com.kyoroteam.kyoro;

import static org.junit.Assert.assertTrue;

import java.util.HashMap;
import java.util.Map;

import com.amazonaws.services.lambda.runtime.Context;

import org.junit.Test;
import org.mockito.Mockito;
/**
 * Unit test for simple App.
 */
public class AppTest 
{
    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue()
    {
        var handler = new Handler();
        var request = new HashMap<String, String>();
        var context = Mockito.mock(Context.class);
        request.put("request", "この言語は少しばかげているように見える");
        var results = handler.handleRequest(request, context);
        System.out.print(results);
        assertTrue( true );
    }
}
