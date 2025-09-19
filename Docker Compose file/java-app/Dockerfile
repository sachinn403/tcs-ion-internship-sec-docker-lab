# Use Maven to build
FROM maven:3.9.6-eclipse-temurin-17 AS builder
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

# Use JDK to run
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=builder /app/target/demo-1.0.0.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
