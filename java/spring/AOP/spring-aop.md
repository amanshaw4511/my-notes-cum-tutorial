
Weaving -  the process of impementing AOP
Weaver -  the framework is used for AOP


aspect -> 
    + pointcut -> 
        expression contains the fully qualified name location of package/class/ method
    + advice -> 
        @Before
        @After
        @Around

joinPoint -> execution instance to be intercepted



@Aspect
@Configuration
class Aspect {

    @Before("execution(* com.aman.*.*(..))")
    void before(JoinPoint joinPoint) {

    }
}


