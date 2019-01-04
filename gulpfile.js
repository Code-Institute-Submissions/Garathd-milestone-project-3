var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function() {
    return gulp.src('static/scss/styles.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/css/'));
});

gulp.task('sass:watch', function() {
    gulp.watch('static/scss/*.scss', gulp.series('sass'));
});