from app import db


class DiseaseData(db.Model):
    """This class represents the bucketlist table."""

    __tablename__ = 'disease_data'
    id = db.Column(db.Integer, primary_key=True)
    disease_name = db.Column(db.String(200))
    disease_signs = db.Column(db.String(2000))
    disease_symptoms = db.Column(db.String(2000))
    confirmatory_tests = db.Column(db.String(400))

    def __init__(self, disease_name, disease_signs, disease_symptoms, confirmatory_tests):
        self.disease_name = disease_name
        self.disease_signs = disease_signs
        self.disease_symptoms = disease_symptoms
        self.confirmatory_tests = confirmatory_tests


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return DiseaseData.query.all()

    def __repr__(self):
        return "<DiseaseData: {}>".format(self.disease_name)
