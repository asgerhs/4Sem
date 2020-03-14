package dk.asgerhs.basics

import java.time.LocalDate

open class Person(val firstName: String, val lastName: String, val dateOfBirth: LocalDate)

fun main() {
    val kurt = Person("William", "Svansfield", LocalDate.of(1997, 11, 1))
    println("Hello ${kurt.firstName} from ${kurt.dateOfBirth}")
}

class Employee(firstName: String, lastName: String,
               dateOfBirth: LocalDate, val dateofEmployement: LocalDate,
               val salary: Int, department: Department)
                : Person( firstName, lastName, dateOfBirth)

class Department(val code : String, val name: String, val manager: Person){
    val employees = mutableListOf<Employee>()
}