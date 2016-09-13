from model_interview import *


class InterviewSlot(BaseModel):

    slot_id = PrimaryKeyField()
    date = DateField()
    time = TimeField()

    # @classmethod
    # def filter(cls, filt=None, data=None):
    #     all_data = []
    #     query = (
    #         cls
    #         .select(cls, Mentor, Applicant)
    #         .join(Mentor)
    #         .join(Applicant, JOIN.LEFT_OUTER, on=InterviewSlot.applicant == Applicant.basic_id)
    #         .where(filt == data))
    #     for all_info in query:
    #         data = [str(all_info.mentor.name), str(all_info.mentor.school.name), str(all_info.time), str(all_info.hour)]
    #         try:
    #             data.append(str(all_info.applicant.name))
    #         except:
    #             data.append(None)
    #         all_data.append(data)
    #     return all_data
