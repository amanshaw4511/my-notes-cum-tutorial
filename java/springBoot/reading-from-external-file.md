
Let say we have file app.properties
    external.service.url=http://localhost:8080

To use this in code
```
@Value("${external.service.url}")
private String url;
```

and define property file to load
```
@Configuration
@ComponentScan
@PropertySource("classpath:app.properties")
public class App {

}
```
