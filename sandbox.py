# """ This is a sandbox for testing out code snippets. """

# import matplotlib.pyplot as plt
# import nltk
# from nltk.probability import FreqDist
# from nltk.tokenize import word_tokenize

# para = """To begin with I shall first like to explain what big data is and why it has become so important in our lives. Big data is simply data, but with a huge size. Data that is not just voluminous but also growing exponentially with time. Such data sets are so large and complex that it is not possible to store or process them using traditional data management tools. So, how huge can this data be? Social media sites like Facebook generate more than 500 terabytes of new data every day in the form of photos, video uploads, text messages, etc. A single Jet engine can generate more than 10 terabytes of data in 30 minutes of flight time. With many thousand flights per day, generation of data reaches up to many petabytes. Data contained in these sets are not always structured. It can be semi-structured or even unstructured. When such is the size and dimension of data we can well imagine how complicated it must be to process and analyze it. Therefore, modern methods of data analysis are being developed and used to process the information contained in big data sets. Opportunities Now coming to the opportunities that Big Data provides, they are not just limited to healthcare. Big data analysis is now a disruptive technology which has intervened into numerous fields and proved its worth. Healthcare is no exception. Big data has the potential to change the entire dynamics of the healthcare industry and improve the quality of life of people. Healthcare industry is a very large and complicated system. It involves a lot of risks and always demands better care. However, when a large number of patients seek emergency care the complications as well as the cost rise exponentially. In India, many times, we even lack sufficient infrastructure to support the patients, there is a deficit of beds as well as doctors to provide treatment to the patients. For instance, when epidemics break out and lives are lost at a very alarming rate, we can easily gauge our helplessness. However, the scenario is certainly improving now. With the advent of digitization into the healthcare system, healthcare providers or practitioners are now having access to a huge amount of patient health data. This healthcare big data can be processed and analyzed to identify patient patterns more quickly and effectively. The information obtained can be extremely useful to figure out chronic health issues and provide preventive treatment plans well beforehand so as to curb that disease or disorder from occurring. This method is also known as predictive analysis and it is one of the most crucial benefits of big data in healthcare. This technology can help the healthcare industry in more ways than we can infer. Healthcare organizations that have implemented predictive analysis have witnessed a reduction in ER visits by providing support and care to patients and decreasing emergency situations. Apart from reduced ER visits and timely treatment, there are many other benefits of big data and predictive analysis. Patients with high-risk life-threatening issues can be provided with more customized treatment facilities. Due to lack of data, there exists a lack of proper planning in hospitals. Under or over-booking of staff, lack of medical equipment, medicines, and other facilities are a result of inefficient budgeting and ill-management of finances. Using predictive analysis these problems can be solved which will lead to reduced costs and efficient management of finances. Better staff allocation and admission rate prediction shall facilitate improvement in daily operations of healthcare organizations. By using big data the effect of recency bias could be reduced as well. When we give more importance to recent events and tend to ignore the effect of the older ones, it may lead to incorrect decisions. This is known as recency bias. Big data also helps in preventing fraudulent activities which in turn prevents losses of insurance companies. Challenges While all of this is changing the healthcare industry for the better, it is not that easy to reap the benefits of big data. There are a whole lot of challenges and vulnerabilities attached to its implementation. One of the biggest challenges is security. Healthcare big data contains the personal information and health history of patients. Acts of hacking, cyber theft and phishing pose a serious threat to these databases. Such data could be stolen and sold for huge sums of money. Protection of the patients’ privacy hence is a serious challenge to big data implementation. Also, the data would contain external data apart from medical information. The organization, therefore, has to take care of privacy, legal compliances, and government policies. Privacy and security of patients have to be given utmost importance and no breach of any kind can be permitted. The next challenge is data classification and modeling. The size of the data is massive and it is less structured and heterogeneous. Classifying such massive data to identify relevant information is a big challenge. Modeling of such unstructured data is equally difficult. Storage and retrieval is another major challenge. Huge cloud servers with sufficient space are required to store such voluminous data. Also, the speed should be high so that uploading of data can be done hassle-free. The way storage is a challenge, retrieval also is a matter of concern. Integrating the data and getting all relevant systems to link each other is a tough job. The next challenge is a major one in my opinion. Finding the right talent who own the expertise to implement this modern technology is an arduous task. Shortage of required talent is a crisis in the market today. Even after hiring the right talent it is a challenge to retain them. Scarce resources like data scientists are hard to find and even harder to retain. They are easily poached by competitors. A good and efficient compensation strategy, conducive work environment, high incentives, opportunities for career growth and development can be some of the ways of retaining such intellectual talent. In a nutshell, we can conclude that while big data is a disruptive technology which will bring about landmark changes in healthcare dynamics, the challenges and vulnerabilities need to be addressed with the utmost care and sense of responsibility."""

# # sentences = nltk.sent_tokenize(para)
# # for text in sentences:
# #     print(text, "\n")

# words = word_tokenize(para, language="english")


# fdist = FreqDist(words)

# print(fdist.most_common(5))


# fdist.plot(30, cumulative=False)
# plt.show()


from fastapi import FastAPI, UploadFile, File
import uvicorn

app = FastAPI()


@app.get("/ping")
async def ping():
    return "Hemlo, Chai Pimlo!"


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
