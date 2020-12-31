using System;
using System.Collections.Generic;

namespace backend
{
    public class Translation
    {
        public int id { get; set; } 
        public List<string> tags { get; set; } 
        public string language { get; set; } 
        public string sentence { get; set; } 
        public object audio_uri { get; set; } 
    }

    public class JibikiSentenceResponse
    {
        public int id { get; set; } 
        public List<string> tags { get; set; } 
        public string language { get; set; } 
        public string sentence { get; set; } 
        public string audio_uri { get; set; } 
        public List<Translation> translations { get; set; } 
    }
}
