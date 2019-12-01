(ns day1.core
  (:require [clojure.string :as str]
            [clojure.edn :as edn])
  (:gen-class))

(defn input
  [] (->> (slurp "input")
          (str/split-lines)
          (map edn/read-string)))

(defn fuel [mass]
  (- (int (/ mass 3)) 2))

(defn rec-fuel
  ([mass] (rec-fuel mass 0))
  ([mass ack]
    (if (< mass 9)
      ack
      (do
        (def next-mass (fuel mass))
        (def next-ack (+ ack next-mass))
        (rec-fuel next-mass next-ack)))))

(defn -main
  [& args]
  (def answer-one (reduce + (map fuel (input))))
  (def answer-two (reduce + (map rec-fuel (input))))
  (println "a) " answer-one)
  (println "b) " answer-two))