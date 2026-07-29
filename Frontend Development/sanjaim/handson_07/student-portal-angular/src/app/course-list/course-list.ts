import { Component, OnInit, inject, signal, computed } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { CourseCard } from '../course-card/course-card';
import { CourseService, Course } from '../course';

@Component({
  selector: 'app-course-list',
  imports: [CommonModule, FormsModule, CourseCard],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})
export class CourseList implements OnInit {
  private courseService = inject(CourseService);

  courses = signal<Course[]>([]);
  loading = signal(false);
  searchTerm = signal('');

  filteredCourses = computed(() =>
    this.courses().filter((course) =>
      course.name.toLowerCase().includes(this.searchTerm().toLowerCase())
    )
  );

  ngOnInit() {
    this.loading.set(true);
    this.courseService.getCourses().subscribe((courses) => {
      this.courses.set(courses);
      this.loading.set(false);
    });
  }

  trackById(index: number, course: Course) {
    return course.id;
  }
}
