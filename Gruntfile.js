module.exports = function(grunt) {

  grunt.initConfig({
    less: {
      main: {
        files: {
          'application_styles/main.css':'application_styles/main.less'
        }
      },
      bootstrap: {
        files: {
          'board/static/css/lib/bootstrap.css':'bower_components/bootstrap/less/bootstrap.less'
        }
      }
    },
    copy: {
      bootstrapVars: {
        src: 'application_styles/variables.less',
        dest: 'bower_components/bootstrap/less/variables.less'
      },
      bootstrapJS: {
        src: 'bower_components/bootstrap/dist/js/bootstrap.min.js',
        dest: 'board/static/js/libs/bootstrap.min.js'
      }
    },
    autoprefixer: {
      dist: {
        files: {
          'board/static/css/main.css':'application_styles/main.css'
        }
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-autoprefixer');

  grunt.registerTask('default',['copy','less','autoprefixer']);

};
