# Custom annotation

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface TrackTime {

}


class CommonPointcutConfig {
    @Pointcut("@annotation(com.aman.aop.TrackTime)")
    void timeTrackAnnotation() {}
}


@Aspect
class Aspects {
    @Around("com.aman.aop.timeTrackAnnotation")
        void trackTime(ProceedingJoinPoint proceedingJoinPoint) {
            ..
            proceedingJoinPoint.proceed();
            ..
        }
}


class Example {
    @TrackTime
    public void calculation() {
        // expensive calculation
    }
}


