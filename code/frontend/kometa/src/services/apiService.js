// src/services/apiService.js
import PocketBase from 'pocketbase';

const pb = new PocketBase(import.meta.env.VITE_POCKETBASE_URL || 'http://127.0.0.1:8090');

export const fetchIdea = async (id) => {
  try {
    const record = await pb.collection('ideas').getOne(id);
    return {
      id: record.id,
      headline: record.idea_output?.concept?.headline,
      description: record.idea_output?.concept?.description,
      pricing: record.idea_output?.concept?.pricing,
      marketing: record.idea_output?.concept?.marketing,
      stand_out: record.idea_output?.concept?.stand_out,
      dos: record.idea_output?.concept?.dos,
      donts: record.idea_output?.concept?.donts,
      milestone_plan: record.idea_output?.plans?.milestone_plan,
      gant_chart: record.idea_output?.plans?.gant_chart,
      raid_chart: record.idea_output?.plans?.raid_chart,
      task_table: record.idea_output?.plans?.task_table,
    };
  } catch (error) {
    console.error('Error fetching idea:', error);
    throw error;
  }
};

export const fetchIdeaDetails = async (ideaId) => {
  try {
    const record = await pb.collection('idea_details').getList(1, 1, {
      filter: `idea_id = "${ideaId}"`,
    });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      return {
        target_audience: item.target_audience,
        pricing: item.pricing,
        marketing: item.marketing,
        stand_out: item.stand_out,
        dos: item.dos,
        donts: item.donts,
      };
    }
  } catch (error) {
    console.error('Error fetching idea details:', error);
    throw error;
  }
};

export const fetchIdeaPlans = async (ideaId) => {
  try {
    const record = await pb.collection('idea_plans').getList(1, 1, {
      filter: `idea_id = "${ideaId}"`,
    });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      return {
        milestone_plan: item.milestone_plan,
        gantt_chart: item.gantt_chart,
        raid_chart: item.raid_chart,
      };
    }
  } catch (error) {
    console.error('Error fetching idea plans:', error);
    throw error;
  }
};

export const fetchIdeaQuality = async (ideaId) => {
  try {
    const record = await pb.collection('idea_quality').getList(1, 1, {
      filter: `idea_id = "${ideaId}"`,
    });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      return {
        originality: item.originality,
        feasibility: item.feasibility,
        difficulty: item.difficulty,
        profitability: item.profitability,
        description: item.description,
      };
    }
  } catch (error) {
    console.error('Error fetching idea quality:', error);
    throw error;
  }
};

export const fetchIdeaScamper = async (ideaId) => {
  try {
    const record = await pb.collection('idea_scamper').getList(1, 1, {
      filter: `idea_id = "${ideaId}"`,
    });
    if (record.items && record.items.length > 0) {
      const item = record.items[0];
      return {
        substitute: item.substitute,
        combine: item.combine,
        adapt: item.adapt,
        modify: item.modify,
        put_to_other_use: item.put_to_other_use,
        eliminate: item.eliminate,
        rearrange: item.rearrange,
      };
    }
  } catch (error) {
    console.error('Error fetching idea scamper:', error);
    throw error;
  }
}
