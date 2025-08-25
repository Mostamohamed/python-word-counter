@Library('shared-lib-2') _

node() {
    // نعرف parameters
    properties([
        parameters([
            string(name: 'PARALLEL_WORKERS', defaultValue: '2', description: 'عدد الـ Workers اللي يشتغلوا parallel')
        ])
    ])

    // نجيب عدد الـ workers باستخدام bounds.groovy
    def workers = bounds.toInt(params.PARALLEL_WORKERS, 1, 5)

    stage('Checkout') {
        checkout([$class: 'GitSCM',
            branches: [[name: "*/main"]],
            userRemoteConfigs: [[
                url: 'https://github.com/Mostamohamed/python-word-counter.git',
                credentialsId: 'github'
            ]]
        ])
    }

    // نجهز الـ jobs
    def jobs = [:]
    for (int i = 1; i <= workers; i++) {
        def idx = i
        jobs["Worker-${idx}"] = {
            stage("Run Worker-${idx}") {
                sh "python3 word_counter.py input.txt output_${idx}.txt"
            }
            stage("Test Worker-${idx}") {
                sh """
                python3 -m venv .venv || true
                . .venv/bin/activate
                pip install -r requirements.txt
                pytest -q || true
                """
            }
        }
    }

    stage('Parallel Execution') {
        parallel jobs
    }
}
