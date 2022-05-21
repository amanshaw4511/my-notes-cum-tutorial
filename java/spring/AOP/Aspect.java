

@Aspect
@Configuration
class Aspect {

    @Before("execution(* com.aman....)")
    public void before(JoinPoint joinPoint) {
        System.out.println("before --> " + joinPoint);
    }

}
