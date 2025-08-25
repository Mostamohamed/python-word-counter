@Library('shared-lib-2') _

node() {
    // تعريف parameters
    properties([
        parameters([
            string(name: 'PARALLEL_WORKERS', defaultValue: '2', description: 'عدد الـ Workers اللي يشتغلوا parallel')
        ])
    ])

    // نجيب عدد الـ workers باستخدام shared lib (bounds.groovy)
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

    // تجهيز الـ jobs
    def jobs = [:]
    for (int i = 1; i <= workers; i++) {
        def idx = i
        jobs["Worker-${idx}"] = {
            stage("Run Worker-${idx}") {
                runWordCounter(idx)
            }
            stage("Test Worker-${idx}") {
                sh """
                python3 -m venv .venv || true
                . .venv/bin/activate
                pip install -r requirements.txt
                PYTHONPATH=. pytest -q || true
                """
            }
        }
    }

    // تنفيذ الـ jobs في parallel
    stage('Parallel Execution') {
        parallel jobs
    }
}
